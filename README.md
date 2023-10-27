# star_sn

star_sn is a backend python based service to perform basic social network operations

## Routing
- POST /user/users/ (Creates new user)
- GET /user/users/ (User activity endpoint which shows when user was login last time and when he made last request to the service)
- GET /user/users/{id} (Get short info about user)
- GET /user/users/{id}/detail/ (Get detailed info about user including last_activity and last_login fields)
- POST /api/token/ (User login & new JWT token generation) (Token is required to make post related requests)
______
- GET /post/posts/ (Get all existing posts)
- POST /post/posts/ (Create a post with 'title' and 'content' fields in request body)
- GET /post/posts/{post_id}/ (Get spesific post) (Same with PUT, PATCH, DELETE. Only owner can change/delete post)
- GET /post/posts/?date_from=YYY-MM-DD&date_to=YYY-MM-DD (Get existing posts within 'date_from - date_to' interval)
- GET /post/analytics/?date_from=YYY-MM-DD&date_to=YYY-MM-DD (Returns likes and posts within 'date_from - date_to' interval.
  Returns all likes and posts if send without parameters)
- GET post/posts/{post_id}/like (Likes the post) (Make same request to unlike a post)

## Getting started with social network api

### Running with Docker
Building
```
docker-compose build star-sn
```

Spinning up
```
docker-compose up star-sn
```

### (optional )Run bot.py to fill database with users and posts after spinnig up the container
