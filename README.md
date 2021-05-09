# Kasich Bogdan KM-83 Lab work 3

Here's my site: https://db-lab3.herokuapp.com which shows the statistics of youtube videos and channels.
There you can see two tables:
1. Channels: channel_name(pk), subscribers.
2. Videos: link(pk), video_name, channel_name(fk), views, rating.

You can press buttons in the top-left corner to show/hide tables.
You can edit rows, but not their primary keys, however you can change the foreign key, but only if it's exist in the parent table.
You can delete rows.(take note that if you delete row in parent table, the orphan rows in child table would be deleted too)
You can create rows with meaningful values(or not so :D), also watch out for primary key duplication.


If you want to interpret site by yourself:

1. Download repository
2. Install flask and flask_sqlalchemy
3. Set: app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://your_login:your_password@localhost/your_database' in app.py
4. Run app.py
5. Check localhost:5000


ERD:

![erdellio](https://user-images.githubusercontent.com/44712899/117588362-80f23880-b12b-11eb-9a0c-b9a7a00bae5d.png)

