rs.initiate({
    _id: "shard03",
    version: 1,
    members: [
        { _id: 0, host: "principal_c:27017" },
        { _id: 1, host: "secondaire_c_1:27017" },
        { _id: 2, host: "secondaire_c_2:27017" },
        { _id: 3, host: "secondaire_c_3:27017" }
    ]
});