
docker-compose exec config01 sh -c "mongosh --port 27017 < /scripts/init-configserver.js"

docker-compose exec principal_a sh -c "mongosh --port 27017 < /scripts/init-shard01.js"

docker-compose exec principal_b sh -c "mongosh --port 27017 < /scripts/init-shard02.js"

docker-compose exec principal_c sh -c "mongosh --port 27017 < /scripts/init-shard03.js"


@echo off
echo WAIT 20s : CONFIGURATION OF THE REPLICATS 
timeout /t 20 /nobreak
echo Fin de la pause


docker-compose exec router1 sh -c "mongod"

docker-compose exec router1 sh -c "mongosh < /scripts/init-router.js"

docker-compose exec router1 sh -c "mongosh < /scripts/users.js"

docker-compose exec router2 sh -c "mongod"

docker-compose exec router2 sh -c "mongosh < /scripts/init-router.js"

docker-compose exec router2 sh -c "mongosh < /scripts/users.js"