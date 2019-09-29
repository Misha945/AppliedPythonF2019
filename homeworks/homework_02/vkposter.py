#!/usr/bin/env python
# coding: utf-8


class VKPoster:

    def __init__(self):
        self.users = {}
        # Ключи - айдишники пользователей.
        # Элементы - списки из их подписчиков.
        self.posts = {}
        # Ключи - айдишники постов
        # Элементы - списки из айдишников просмотревших (создатель первый).

    def user_posted_post(self, user_id: int, post_id: int):
        if user_id not in self.users.keys():
            self.users.update({user_id: []})
        self.posts.update({post_id: [user_id]})
        '''
        Метод который вызывается когда пользователь user_id
        выложил пост post_id.
        :param user_id: id пользователя. Число.
        :param post_id: id поста. Число.
        :return: ничего
        '''

    def user_read_post(self, user_id: int, post_id: int):
        if user_id not in self.users.keys():
            self.users.update({user_id: []})
        self.posts[post_id].append(user_id)
        '''
        Метод который вызывается когда пользователь user_id
        прочитал пост post_id.
        :param user_id: id пользователя. Число.
        :param post_id: id поста. Число.
        :return: ничего
        '''

    def user_follow_for(self, follower_user_id: int, followee_user_id: int):
        if followee_user_id not in self.users.keys():
            self.users.update({followee_user_id: [follower_user_id]})
        else:
            self.users[followee_user_id].append(follower_user_id)
        '''
        Метод который вызывается когда пользователь follower_user_id
        подписался на пользователя followee_user_id.
        :param follower_user_id: id пользователя. Число.
        :param followee_user_id: id пользователя. Число.
        :return: ничего
        '''

    def get_recent_posts(self, user_id: int, k: int) -> list:
        following = []
        for i in self.users.keys():
            if user_id in self.users[i]:
                following.append(i)
        posts = []
        for i in self.posts.keys():
            if self.posts[i][0] in following:
                posts.append(i)
        posts.sort()
        posts.reverse()
        while len(posts) > k:
            posts.pop()
        return posts
        '''
        Метод который вызывается когда пользователь user_id
        запрашивает k свежих постов людей на которых он подписан.
        :param user_id: id пользователя. Число.
        :param k: Сколько самых свежих постов необходимо вывести. Число.
        :return: Список из post_id размером К из свежих постов в
        ленте пользователя. list
        '''

    def get_most_popular_posts(self, k: int) -> list:
        popularity = {}
        # Ключи - кол-во просмотревших, элементы - айди постов (всех)
        for i in self.posts.keys():
            wc = []
            for k in self.posts[i]:
                if k not in wc:
                    wc.append(k)
            popularity.update({len(wc): i})
        L = list(popularity.keys)
        L.sort()
        L.reverse()
        Result = []
        for i in L:
            Result.append(popularity[i])
            if len(Result) == k:
                break
        return Result
        '''
        Метод который возвращает список k самых популярных постов за все время,
        остортированных по свежести.
        :param k: Сколько самых свежих популярных постов
        необходимо вывести. Число.
        :return: Список из post_id размером К из популярных постов. list
        '''
