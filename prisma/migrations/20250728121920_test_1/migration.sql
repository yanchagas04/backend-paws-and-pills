-- AlterTable
ALTER TABLE "Cat" ADD COLUMN     "image" TEXT;

-- AlterTable
ALTER TABLE "Dog" ADD COLUMN     "image" TEXT,
ALTER COLUMN "deletedAt" DROP NOT NULL;

-- AlterTable
ALTER TABLE "Dose" ALTER COLUMN "deletedAt" DROP NOT NULL;

-- AlterTable
ALTER TABLE "Medicine" ALTER COLUMN "deletedAt" DROP NOT NULL;

-- AlterTable
ALTER TABLE "User" ADD COLUMN     "image" TEXT,
ALTER COLUMN "deletedAt" DROP NOT NULL;
