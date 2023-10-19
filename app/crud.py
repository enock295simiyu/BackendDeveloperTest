from sqlalchemy import select
from sqlalchemy.orm import Session

from app.exceptions import PostInfoNotFoundError, PostInfoDoesNotBelongToYouError
from app.models import PostInfo
from app.schemas import CreateAndUpdatePost


async def get_all_posts(session: Session, limit: int, offset: int, user):
    results = await session.execute(select(PostInfo).offset(offset).limit(limit))
    return results.scalars().all()


async def get_users_posts(session: Session, user, limit: int, offset: int):
    stmt = select(PostInfo).offset(offset).limit(limit).filter(PostInfo.user_id == str(user.id))
    result = await session.execute(stmt)
    user_posts = result.scalars().all()

    return user_posts


# Function to  get info of a particular post
async def get_post_info_by_id(session: Session, _id: int) -> PostInfo:
    post_info = await session.get(PostInfo, _id)

    if post_info is None:
        raise PostInfoNotFoundError

    return post_info


# Function to add a new post info to the database
async def create_post(session: Session, post_info: CreateAndUpdatePost, user) -> PostInfo:
    data = post_info.dict()
    data['user_id'] = str(user.id)
    new_post_info = PostInfo(**data)
    session.add(new_post_info)
    await session.commit()
    await session.refresh(new_post_info)
    return new_post_info


# Function to update details of the post
async def update_post_info(session: Session, post_id: int, info_update: CreateAndUpdatePost, user) -> PostInfo:
    post_info = await get_post_info_by_id(session, post_id)

    if post_info is None:
        raise PostInfoNotFoundError

    if post_info.user_id != str(user.id):
        raise PostInfoDoesNotBelongToYouError

    post_info.title = info_update.title
    post_info.content = info_update.content

    await session.commit()

    return post_info


# Function to delete a post info from the db
def delete_post_info(session: Session, _id: int):
    post_info = get_post_info_by_id(session, _id)

    if post_info is None:
        raise PostInfoNotFoundError

    session.delete(post_info)
    session.commit()

    return
