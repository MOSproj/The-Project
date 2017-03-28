#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pymongo


class Database:

    def __init__(self, db_path, db_name, username, password):
        self.db = self.__get_connection(db_path, db_name, username, password)

    def get_db(self):
        return self.db

    def get_categories(self):
        return self.db.categories.find()

    def get_groups(self):
        return self.db.groups.find()

    def get_post(self, post_id):
        return self.db.posts.find_one({"id": post_id})

    def insert_post(self, post):
        try:
            self.db.posts2.insert(post)
        except pymongo.errors.DuplicateKeyError, e:
            print e

    def update_post(self, post, update=False):
        try:
            self.db.posts2.update({'id': post['id']}, post, {'upsert': update})
        except pymongo.errors, e:
            print e

    def set_ignore(self, post_id):
        self.db.posts.save({"id": post_id}, {
            "id": post_id,
            "ignore": True
        })

    def if_exists(self, post_id):
        return type(self.get_post(post_id)) is dict

    def __get_connection(self, db_path, db_name, username, password):
        db_full_path = 'mongodb://'
        if len(username) > 0:
            db_full_path += username + ':' + password + '@'
        db_full_path += db_path
        if len(db_name) > 0:
            db_full_path += '/' + db_name

        connection = pymongo.MongoClient(db_full_path)
        return connection[db_name]