import io

import pandas as pd
from fastapi import FastAPI, Form, HTTPException, UploadFile
from fastapi.responses import PlainTextResponse
from sqlalchemy import text

from database.database import engine
from database.models import department, employee, job

app = FastAPI()

tables_enum = {"job": job, "department": department, "employee": employee}


def _upsert(table, conn, keys, data_iter):
    from sqlalchemy.dialects.postgresql import insert

    data = [dict(zip(keys, row)) for row in data_iter]

    insert_statement = insert(table.table).values(data)
    upsert_statement = insert_statement.on_conflict_do_update(
        constraint=f"{table.table.name}_pkey",
        set_={c.key: c for c in insert_statement.excluded},
    )
    conn.execute(upsert_statement)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/upload")
async def create_upload_file(
    file: UploadFile,
    table: str = Form(),
    start_row: int | None = Form(default=None, ge=1, le=1000),
    end_row: int | None = Form(default=None, gt=1, le=1000),
):
    if table in tables_enum:
        content = await file.read()
        with io.BytesIO(content) as data:
            if "csv" in file.content_type:
                if start_row and end_row:
                    if start_row <= end_row:
                        df = pd.read_csv(
                            data,
                            names=tables_enum.get(table).columns.keys(),
                            skiprows=start_row - 1,
                            nrows=end_row - start_row,
                        )
                        print(df)
                    else:
                        raise HTTPException(
                            status_code=400, detail="Invalid parameters"
                        )
                else:
                    df = pd.read_csv(data, names=tables_enum.get(table).columns.keys())
            else:
                raise HTTPException(status_code=400, detail="Invalid file")
        try:
            conn = engine.connect()
            df.to_sql(
                table,
                schema="public",
                con=conn,
                index=False,
                if_exists="append",
                method=_upsert,
            )
        except Exception as e:
            raise HTTPException(status_code=409, detail=f"Couldn't upload file\n{e}")

        return {"Uploaded succesfully"}
    else:
        raise HTTPException(status_code=400, detail="Invalid table name")


@app.get("/employee/department/job")
async def root():
    with engine.connect() as conn:
        with open("database/queries/hirings_by_q.sql") as file:
            query = text(file.read())
            execution = conn.execute(query)
            column_names = execution.keys()
            result = execution.fetchall()
            result_list = [dict(zip(column_names, row)) for row in result]
    return PlainTextResponse(str(result_list))


@app.get("/department/employee")
async def root():
    with engine.connect() as conn:
        with open("database/queries/higher_than_avg.sql") as file:
            query = text(file.read())
            execution = conn.execute(query)
            column_names = execution.keys()
            result = execution.fetchall()
            result_list = [dict(zip(column_names, row)) for row in result]
    return PlainTextResponse(str(result_list))
