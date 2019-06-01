# Databases course work
### Got data from
+ thomann.de
+ muztorg.ua
+ reverb.com
### Analysis
+ Quantity of guitars in price range (muztorg, thomann)
+ Quantity of guitars by manufacturer (muztorg, thomann)
+ Shipping prices from different regions (reverb)
+ Shipping prices for specified manufacturer (reverb)
+ Shipping prices for specified region and manufaсturer (reverb)

### To start database 
1. create data/db1-9 if not exists

2. sudo mongod --shardsvr --port {port} --dbpath ./data/db{num} --replSet replsetName
    * port 27001-27003 num 1-3 replsetName = rs0
    * port 27004-27006 num 4-6 replsetName = rs1

3. sudo mongod --configsvr --port {port} --dbpath ./data/db{num} --replSet config
    * port 27007-27009 num 7-9
4. sudo mongos --configdb config/localhost:27007,localhost:27008,localhost:27009 --port 27010

 
