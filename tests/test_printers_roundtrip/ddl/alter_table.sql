ALTER TABLE t1 ALTER c1 TYPE varchar(20)

ALTER TABLE t1 ALTER c1 TYPE montype USING mafonction(c1)

ALTER TABLE t1 OWNER TO role1

ALTER TABLE t1 ALTER c1 SET STATISTICS 1000

ALTER TABLE t1 ALTER COLUMN c1 SET STORAGE EXTERNAL

ALTER TABLE t1 ALTER C1 SET DEFAULT 'default'

ALTER TABLE IF EXISTS t1 ALTER C1 DROP DEFAULT

ALTER TABLE t1 ADD COLUMN IF NOT EXISTS c1 int

ALTER TABLE t2 DROP COLUMN IF EXISTS c1

ALTER TABLE t2 DROP COLUMN IF EXISTS c1 CASCADE

ALTER TABLE t2 ENABLE TRIGGER trig1

ALTER TABLE t2 DISABLE TRIGGER trig1

ALTER TABLE t1 ALTER COLUMN c1 DROP NOT NULL

ALTER TABLE t1 ALTER COLUMN c2 SET NOT NULL

ALTER TABLE t1 ADD FOREIGN KEY (c1) REFERENCES t2(c1) DEFERRABLE INITIALLY DEFERRED NOT VALID

ALTER TABLE t1 DROP CONSTRAINT IF EXISTS c1_check

ALTER TABLE t1 CLUSTER ON c1_idx

ALTER TABLE t1 ENABLE ROW LEVEL SECURITY

ALTER TABLE t1 DISABLE ROW LEVEL SECURITY

ALTER TABLE t1 VALIDATE CONSTRAINT c1_check

ALTER TABLE t1 ADD PRIMARY KEY USING INDEX t1_idx

ALTER TABLE t1 ADD CONSTRAINT con1 UNIQUE USING INDEX t1_idx DEFERRABLE INITIALLY DEFERRED

ALTER TABLE t1 ADD CONSTRAINT con1 EXCLUDE USING gist (f WITH OPERATOR(intarray.&&))

ALTER FOREIGN TABLE c1 ADD COLUMN c1 int

ALTER TABLE t1 RENAME CONSTRAINT con1 TO con2

ALTER INDEX idx1 ALTER COLUMN c1 SET STATISTICS 100

ALTER INDEX idx1 ALTER COLUMN 2 SET STATISTICS 100

ALTER TABLE t1 SET LOGGED

ALTER TABLE t1 SET UNLOGGED

ALTER TABLE t1 ALTER COLUMN c1 RESTART

ALTER TABLE t1 ALTER COLUMN c1 RESTART WITH 42

ALTER TABLE t1 ALTER COLUMN c1 SET CACHE 1

ALTER TABLE t1 ALTER COLUMN c1 SET CYCLE

ALTER TABLE t1 ALTER COLUMN c1 SET NO CYCLE

ALTER TABLE t1 ALTER COLUMN c1 SET NO MAXVALUE

ALTER TABLE t1 ALTER COLUMN c1 SET MAXVALUE 1

ALTER TABLE t1 ALTER COLUMN c1 SET NO MINVALUE

ALTER TABLE t1 ALTER COLUMN c1 SET MINVALUE 1

ALTER TABLE t1 ALTER COLUMN c1 SET SEQUENCE NAME foo

ALTER TABLE t1 ENABLE REPLICA TRIGGER foo

ALTER TABLE x ADD UNIQUE (k) WITH (foo='bar', bar='foo')

ALTER TABLE ALL IN TABLESPACE foo OWNED BY me SET TABLESPACE bar NOWAIT
