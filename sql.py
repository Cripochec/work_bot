import sqlite3 as sq
bd = sq.connect('site.db')
cur = bd.cursor()
bd.row_factory = sq.Row


async def bd_start():
    global bd, cur
    bd = sq.connect('site.db')
    cur = bd.cursor()

    cur.execute("""CREATE TABLE IF NOT EXISTS all_site(
                site_id INTEGER PRIMARY KEY AUTOINCREMENT,
                site TEXT )""")
    bd.commit()


async def bd_all_site():
    all_site_select = cur.execute("SELECT * FROM all_site").fetchall()
    all_site = ''
    for el in all_site_select:
        all_site += el[0] + ') ' + el[1] + '\n'
    return all_site


async def bd_add_account(new_site):
    cur.execute(f"""INSERT INTO all_site(site) 
       VALUES({new_site});""")
    bd.commit()


async def bd_del_account(del_id):
    cur.execute(f"DELETE FROM all_site WHERE site_id={del_id};")
    bd.commit()

all_site_select = cur.execute("SELECT * FROM all_site").fetchall()
all_site = ''
for el in all_site_select:
    all_site += el[0]
print(all_site)