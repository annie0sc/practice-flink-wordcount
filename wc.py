from pyflink.dataset import ExecutionEnvironment
from pyflink.table import TableConfig, DataTypes, BatchTableEnvironment
from pyflink.table.descriptors import Schema, OldCsv, FileSystem
import wcpretreatment as wpre
import os
import time

start_t = time.time()

exec_env = ExecutionEnvironment.get_execution_environment()
exec_env.set_parallelism(1)
t_config = TableConfig()
t_env = BatchTableEnvironment.create(exec_env, t_config)

input_path = './input/data.json'
output_path = './output/output.txt'
if os.path.exists(output_path):
    os.remove(output_path)

wpre.wcpretreatment(input_path)
input_path = './input'

t_env.connect(FileSystem().path(input_path)) \
    .with_format(OldCsv()
                 .field('geoID', DataTypes.STRING())) \
    .with_schema(Schema()
                 .field('geoID', DataTypes.STRING())) \
    .create_temporary_table('mySource')

t_env.connect(FileSystem().path(output_path)) \
    .with_format(OldCsv()
                 .field_delimiter('\t')
                 .field('geoID', DataTypes.STRING())
                 .field('notification_rate_per_100000_population_14-days', DataTypes.BIGINT())) \
    .with_schema(Schema()
                 .field('geoID', DataTypes.STRING())
                 .field('notification_rate_per_100000_population_14-days', DataTypes.BIGINT())) \
    .create_temporary_table('mySink')

t_env.from_path('mySource') \
    .group_by('geoID') \
    .select('geoID, count(1)') \
    .insert_into('mySink')

t_env.execute("python_job")
os.remove('./input')

print(time.time() - start_t)
