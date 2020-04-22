CREATE TABLE IF NOT EXISTS "event" (
    "id" INTEGER NOT NULL PRIMARY KEY,
    "key" TEXT NOT NULL,
    "timestamp" DATETIME NOT NULL,
    "metadata" TEXT NOT NULL);