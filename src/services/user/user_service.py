from lib.prisma.client import Prisma
from src.schemas.user.user_schema import UserSchema, UserResponseSchema


class UserService:
    prisma = Prisma()

    async def get_user(self, id: str) -> UserResponseSchema:
        await self.prisma.connect()
        try:
            user = await self.prisma.user.find_unique(
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
            print("finally")

    async def create_user(self, user: UserSchema) -> UserResponseSchema:
        await self.prisma.connect()
        try:
            user = await self.prisma.user.create(
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
            print("finally")
        
    async def update_user(self, id: str, user: UserSchema) -> UserResponseSchema:
        await self.prisma.connect()
        try:
            user = await self.prisma.user.update(
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
            print("finally")

    async def delete_user(self, id: str) -> UserResponseSchema:
        await self.prisma.connect()
        try:
            user = await self.prisma.user.delete(
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
            print("finally")