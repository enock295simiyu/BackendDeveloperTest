from fastapi import APIRouter, Depends, HTTPException
from fastapi_restful.cbv import cbv
from sqlalchemy.orm import Session

from app.crud import create_post, get_users_posts
from app.db import get_async_session, User
from app.exceptions import PostInfoException
from app.schemas import PaginatedPostInfo, CreateAndUpdatePost
from app.users import current_active_user

router = APIRouter()


@cbv(router)
class PostsView:
    session: Session = Depends(get_async_session)

    @router.get("/posts", response_model=PaginatedPostInfo)
    async def list_posts(self, limit: int = 10, offset: int = 0, user: User = Depends(current_active_user)):
        """
        This endpoint returns all the posts
        :param user: The current user
        :param limit: The number of post per page
        :param offset: The page number
        :return:
        """
        cars_list = await get_users_posts(self.session, user, limit=limit, offset=offset)
        response = {"limit": limit, "offset": offset, "data": cars_list}

        return response

    @router.post("/posts")
    async def add_post(self, post_info: CreateAndUpdatePost, user: User = Depends(current_active_user)):

        try:
            post_info = await create_post(self.session, post_info, user)
            return post_info
        except PostInfoException as cie:
            raise HTTPException(**cie.__dict__)
