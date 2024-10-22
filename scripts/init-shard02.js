rs.initiate({
    _id: "shard02",
    version: 1,
    members: [
        { _id: 0, host: "principal_b:27017" },
        { _id: 1, host: "secondaire_b_1:27017" },
        { _id: 2, host: "secondaire_b_2:27017" },
        { _id: 3, host: "secondaire_b_3:27017" }
    ]
});