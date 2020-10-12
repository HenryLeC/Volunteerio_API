import os
import dns.resolver

databaseHost = os.environ['DATABASE_HOSTNAME']
databaseDatabase = os.environ['DATABASE_DATABASE']
databaseUsername = os.environ['DATABASE_USERNAME']
databasePass = os.environ['DATABASE_PASSWORD']

SecretKey = os.environ['API_SECRET_KEY']
SECURITY_PASSWORD_SALT = os.environ['API_PASSWORD_SALT']

srv_records = dns.resolver.resolve(databaseHost, 'SRV')
srvInfo = {}
for srv in srv_records:
    srvInfo['port'] = srv.port
    srvInfo['host'] = str(srv.target).rstrip('.')

DatabaseURI = f"postgres://{databaseUsername}:{databasePass}@{srvInfo['host']}:{srvInfo['port']}/{databaseDatabase}?client_encoding=utf8"
