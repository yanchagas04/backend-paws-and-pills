from lib.prisma import Prisma
from src.schemas.user.user_schema import UserSchema, UserResponseSchema

class UserService:

    async def get_user(self, id: str) -> UserResponseSchema:
        await Prisma.connect()
        try:
            user = await Prisma.user.find_unique(
                where={
                    'id': id
                }
            )
            if user:
                return UserSchema(
                    id=user.id,
                    name=user.name,
                    email=user.email,
                    password=user.password,
                    image=user.image
                )
            else:
                return None
        finally:
            await Prisma.close()

    async def create_user(self, user: UserSchema) -> UserResponseSchema:
        await Prisma.connect()
        try:
            user = await Prisma.user.create(
                data={
                    'name': user.name,
                    'email': user.email,
                    'password': user.password,
                    'image': user.image
                }
            )
            return UserResponseSchema(
                status='success',
                user=UserSchema(
                    id=user.id,
                    name=user.name,
                    email=user.email,
                    password=user.password,
                    image=user.image
                )
            )
        finally:
            await Prisma.close()
        
    async def update_user(self, id: str, user: UserSchema) -> UserResponseSchema:
        await Prisma.connect()
        try:
            user = await Prisma.user.update(
                where={
                    'id': id
                },
                data={
                    'name': user.name,
                    'email': user.email,
                    'password': user.password,
                    'image': user.image
                }
            )
            return UserResponseSchema(
                status='success',
                user=UserSchema(
                    id=user.id,
                    name=user.name,
                    email=user.email,
                    password=user.password,
                    image=user.image
                )
            )
        finally:
            await Prisma.close()

    async def delete_user(self, id: str) -> UserResponseSchema:
        await Prisma.connect()
        try:
            user = await Prisma.user.delete(
                where={
                    'id': id
                }
            )
            return UserResponseSchema(
                status='success',
                user=UserSchema(
                    id=user.id,
                    name=user.name,
                    email=user.email,
                    password=user.password,
                    image=user.image
                )
            )
        finally:
            await Prisma.close()