from fastapi import APIRouter, Body, Depends, HTTPException
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession
from app.api.deps import get_db


router = APIRouter()


@router.get("/")  # TEST REQUEST
async def read_root(db: AsyncSession = Depends(get_db)):
    async with db.begin():
        # Execute the SQL query to fetch all records from 'test_table'
        result = await db.execute(text("SELECT * FROM test_table"))
        # Fetch all rows from the result of the query
        result_list = result.fetchall()
        # Convert each row in the result list to a dictionary
        result_data = [dict(row) for row in result_list]

        # Return a dictionary containing a greeting and the result data
        return {"Hello": "World", "Result": result_data}
