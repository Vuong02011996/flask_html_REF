# REF
## Flask
https://gist.github.com/mjul/32d697b734e7e9171cdb


## Mongo

https://www.codegrepper.com/code-examples/typescript/mongodb+array+count

db.identities.aggregate( [  { $project: { _id: 0, count: {$size:"$matching_face_ids" }} }
db.identities.aggregate( [{ $project": { _id: 0, count: {$size:"$matching_face_ids" }} }, { $group: { _id: null, test: {$sum: "$count"}}} ] )