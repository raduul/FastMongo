db.createUser({
  user: 'myappuser',
  pwd: 'mypassword',
  roles: [{
    role: 'readWrite',
    db: 'fast-api'
  }]
});

db.createCollection("sample-users");
