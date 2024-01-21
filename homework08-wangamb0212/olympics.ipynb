{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 153,
   "id": "e5cbbeeb-51c3-435c-8175-3d5af1edba85",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: sqlalchemy in /Users/amber/opt/anaconda3/envs/PythonAmber/lib/python3.9/site-packages (2.0.9)\n",
      "Requirement already satisfied: typing-extensions>=4.2.0 in /Users/amber/opt/anaconda3/envs/PythonAmber/lib/python3.9/site-packages (from sqlalchemy) (4.4.0)\n",
      "Requirement already satisfied: greenlet!=0.4.17 in /Users/amber/opt/anaconda3/envs/PythonAmber/lib/python3.9/site-packages (from sqlalchemy) (2.0.2)\n",
      "Requirement already satisfied: pymysql in /Users/amber/opt/anaconda3/envs/PythonAmber/lib/python3.9/site-packages (1.0.3)\n",
      "Collecting mysql\n",
      "  Using cached mysql-0.0.3-py3-none-any.whl (1.2 kB)\n",
      "Collecting mysqlclient\n",
      "  Using cached mysqlclient-2.1.1.tar.gz (88 kB)\n",
      "  Preparing metadata (setup.py) ... \u001b[?25lerror\n",
      "  \u001b[1;31merror\u001b[0m: \u001b[1msubprocess-exited-with-error\u001b[0m\n",
      "  \n",
      "  \u001b[31m×\u001b[0m \u001b[32mpython setup.py egg_info\u001b[0m did not run successfully.\n",
      "  \u001b[31m│\u001b[0m exit code: \u001b[1;36m1\u001b[0m\n",
      "  \u001b[31m╰─>\u001b[0m \u001b[31m[16 lines of output]\u001b[0m\n",
      "  \u001b[31m   \u001b[0m /bin/sh: mysql_config: command not found\n",
      "  \u001b[31m   \u001b[0m /bin/sh: mariadb_config: command not found\n",
      "  \u001b[31m   \u001b[0m /bin/sh: mysql_config: command not found\n",
      "  \u001b[31m   \u001b[0m Traceback (most recent call last):\n",
      "  \u001b[31m   \u001b[0m   File \"<string>\", line 2, in <module>\n",
      "  \u001b[31m   \u001b[0m   File \"<pip-setuptools-caller>\", line 34, in <module>\n",
      "  \u001b[31m   \u001b[0m   File \"/private/var/folders/m7/t4rg2djd2h90frfplw_4p5080000gn/T/pip-install-ve9461xj/mysqlclient_c31414c1d423457582d6434ec0ee9391/setup.py\", line 15, in <module>\n",
      "  \u001b[31m   \u001b[0m     metadata, options = get_config()\n",
      "  \u001b[31m   \u001b[0m   File \"/private/var/folders/m7/t4rg2djd2h90frfplw_4p5080000gn/T/pip-install-ve9461xj/mysqlclient_c31414c1d423457582d6434ec0ee9391/setup_posix.py\", line 70, in get_config\n",
      "  \u001b[31m   \u001b[0m     libs = mysql_config(\"libs\")\n",
      "  \u001b[31m   \u001b[0m   File \"/private/var/folders/m7/t4rg2djd2h90frfplw_4p5080000gn/T/pip-install-ve9461xj/mysqlclient_c31414c1d423457582d6434ec0ee9391/setup_posix.py\", line 31, in mysql_config\n",
      "  \u001b[31m   \u001b[0m     raise OSError(\"{} not found\".format(_mysql_config_path))\n",
      "  \u001b[31m   \u001b[0m OSError: mysql_config not found\n",
      "  \u001b[31m   \u001b[0m mysql_config --version\n",
      "  \u001b[31m   \u001b[0m mariadb_config --version\n",
      "  \u001b[31m   \u001b[0m mysql_config --libs\n",
      "  \u001b[31m   \u001b[0m \u001b[31m[end of output]\u001b[0m\n",
      "  \n",
      "  \u001b[1;35mnote\u001b[0m: This error originates from a subprocess, and is likely not a problem with pip.\n",
      "\u001b[1;31merror\u001b[0m: \u001b[1mmetadata-generation-failed\u001b[0m\n",
      "\n",
      "\u001b[31m×\u001b[0m Encountered error while generating package metadata.\n",
      "\u001b[31m╰─>\u001b[0m See above for output.\n",
      "\n",
      "\u001b[1;35mnote\u001b[0m: This is an issue with the package mentioned above, not pip.\n",
      "\u001b[1;36mhint\u001b[0m: See above for details.\n",
      "\u001b[?25h"
     ]
    }
   ],
   "source": [
    "!pip install sqlalchemy\n",
    "!pip install pymysql\n",
    "!pip install mysql"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 132,
   "id": "11f7b07f-ec9b-4ccb-a910-f33f0252b3ef",
   "metadata": {},
   "outputs": [],
   "source": [
    "import configparser\n",
    "from operator import itemgetter\n",
    "\n",
    "import sqlalchemy\n",
    "from sqlalchemy import create_engine\n",
    "\n",
    "# columns and their types, including fk relationships\n",
    "from sqlalchemy import Column, Integer, Float, String, DateTime\n",
    "from sqlalchemy import ForeignKey\n",
    "from sqlalchemy.orm import relationship\n",
    "\n",
    "# declarative base, session, and datetime\n",
    "from sqlalchemy.ext.declarative import declarative_base\n",
    "from sqlalchemy.orm import sessionmaker\n",
    "from datetime import datetime"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 133,
   "id": "2d441913-8c48-4231-b65c-c0b0e130fe5b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: psycopg2-binary in /Users/amber/opt/anaconda3/envs/PythonAmber/lib/python3.9/site-packages (2.9.6)\n",
      "Requirement already satisfied: flask in /Users/amber/opt/anaconda3/envs/PythonAmber/lib/python3.9/site-packages (2.2.3)\n",
      "Requirement already satisfied: Jinja2>=3.0 in /Users/amber/opt/anaconda3/envs/PythonAmber/lib/python3.9/site-packages (from flask) (3.1.2)\n",
      "Requirement already satisfied: importlib-metadata>=3.6.0 in /Users/amber/opt/anaconda3/envs/PythonAmber/lib/python3.9/site-packages (from flask) (4.11.3)\n",
      "Requirement already satisfied: click>=8.0 in /Users/amber/opt/anaconda3/envs/PythonAmber/lib/python3.9/site-packages (from flask) (8.0.4)\n",
      "Requirement already satisfied: itsdangerous>=2.0 in /Users/amber/opt/anaconda3/envs/PythonAmber/lib/python3.9/site-packages (from flask) (2.1.2)\n",
      "Requirement already satisfied: Werkzeug>=2.2.2 in /Users/amber/opt/anaconda3/envs/PythonAmber/lib/python3.9/site-packages (from flask) (2.2.3)\n",
      "Requirement already satisfied: zipp>=0.5 in /Users/amber/opt/anaconda3/envs/PythonAmber/lib/python3.9/site-packages (from importlib-metadata>=3.6.0->flask) (3.11.0)\n",
      "Requirement already satisfied: MarkupSafe>=2.0 in /Users/amber/opt/anaconda3/envs/PythonAmber/lib/python3.9/site-packages (from Jinja2>=3.0->flask) (2.1.1)\n",
      "Requirement already satisfied: flask_sqlalchemy in /Users/amber/opt/anaconda3/envs/PythonAmber/lib/python3.9/site-packages (3.0.3)\n",
      "Requirement already satisfied: Flask>=2.2 in /Users/amber/opt/anaconda3/envs/PythonAmber/lib/python3.9/site-packages (from flask_sqlalchemy) (2.2.3)\n",
      "Requirement already satisfied: SQLAlchemy>=1.4.18 in /Users/amber/opt/anaconda3/envs/PythonAmber/lib/python3.9/site-packages (from flask_sqlalchemy) (2.0.9)\n",
      "Requirement already satisfied: importlib-metadata>=3.6.0 in /Users/amber/opt/anaconda3/envs/PythonAmber/lib/python3.9/site-packages (from Flask>=2.2->flask_sqlalchemy) (4.11.3)\n",
      "Requirement already satisfied: Jinja2>=3.0 in /Users/amber/opt/anaconda3/envs/PythonAmber/lib/python3.9/site-packages (from Flask>=2.2->flask_sqlalchemy) (3.1.2)\n",
      "Requirement already satisfied: Werkzeug>=2.2.2 in /Users/amber/opt/anaconda3/envs/PythonAmber/lib/python3.9/site-packages (from Flask>=2.2->flask_sqlalchemy) (2.2.3)\n",
      "Requirement already satisfied: click>=8.0 in /Users/amber/opt/anaconda3/envs/PythonAmber/lib/python3.9/site-packages (from Flask>=2.2->flask_sqlalchemy) (8.0.4)\n",
      "Requirement already satisfied: itsdangerous>=2.0 in /Users/amber/opt/anaconda3/envs/PythonAmber/lib/python3.9/site-packages (from Flask>=2.2->flask_sqlalchemy) (2.1.2)\n",
      "Requirement already satisfied: greenlet!=0.4.17 in /Users/amber/opt/anaconda3/envs/PythonAmber/lib/python3.9/site-packages (from SQLAlchemy>=1.4.18->flask_sqlalchemy) (2.0.2)\n",
      "Requirement already satisfied: typing-extensions>=4.2.0 in /Users/amber/opt/anaconda3/envs/PythonAmber/lib/python3.9/site-packages (from SQLAlchemy>=1.4.18->flask_sqlalchemy) (4.4.0)\n",
      "Requirement already satisfied: zipp>=0.5 in /Users/amber/opt/anaconda3/envs/PythonAmber/lib/python3.9/site-packages (from importlib-metadata>=3.6.0->Flask>=2.2->flask_sqlalchemy) (3.11.0)\n",
      "Requirement already satisfied: MarkupSafe>=2.0 in /Users/amber/opt/anaconda3/envs/PythonAmber/lib/python3.9/site-packages (from Jinja2>=3.0->Flask>=2.2->flask_sqlalchemy) (2.1.1)\n"
     ]
    }
   ],
   "source": [
    "!pip install psycopg2-binary\n",
    "!pip install flask\n",
    "!pip install flask_sqlalchemy"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 160,
   "id": "69be974c-779e-40f7-8feb-cd51adeb5312",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "amber2 wsq0212 Localhost homework08\n",
      "using dsn: postgresql://amber2:wsq0212@Localhost/homework08\n"
     ]
    }
   ],
   "source": [
    "# configuring your database connection\n",
    "config = configparser.ConfigParser()\n",
    "config.read('config.ini')\n",
    "u, pw, host, db = itemgetter('username', 'password', 'host', 'database')(config['db'])\n",
    "print(u, pw, host, db)\n",
    "dsn = f'postgresql://{u}:{pw}@{host}/{db}'\n",
    "print(f'using dsn: {dsn}')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 161,
   "id": "19fe47e1-44fe-4ff7-8c79-bf2bd6cc1381",
   "metadata": {},
   "outputs": [],
   "source": [
    "# from urllib.parse import quote  \n",
    "# from sqlalchemy.engine import create_engine\n",
    "# engine = create_engine('mysql+mysqlconnector://postgres:%s@localhost:5432/database' % quote('wsq0212'))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 162,
   "id": "60582b85-8c9d-4d21-95e6-acce05b115ad",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "/var/folders/m7/t4rg2djd2h90frfplw_4p5080000gn/T/ipykernel_37951/1513570141.py:4: MovedIn20Warning: The ``declarative_base()`` function is now available as sqlalchemy.orm.declarative_base(). (deprecated since: 2.0) (Background on SQLAlchemy 2.0 at: https://sqlalche.me/e/b8d9)\n",
      "  Base = declarative_base()\n"
     ]
    }
   ],
   "source": [
    "# engine = create_engine(dsn, echo=True)\n",
    "engine = create_engine(dsn, echo=True)\n",
    "# engine = create_engine(\"mysql+pymysql://user:pw@host/db\", pool_pre_ping=True)\n",
    "Base = declarative_base()\n",
    "Session = sessionmaker(engine)\n",
    "session = Session()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 163,
   "id": "4bbf3ffc-7045-48d0-a92a-f4ca08cacd35",
   "metadata": {},
   "outputs": [],
   "source": [
    "# TODO: Write classes and code here\n",
    "class AthleteEvent(Base):\n",
    "    __tablename__ = 'AthleteEvent'\n",
    "\n",
    "    # columns\n",
    "    athlete_event_id = Column('athlete_event_id', Integer, primary_key = True)\n",
    "    id = Column('id', Integer)\n",
    "    name = Column('name', String)\n",
    "    age = Column('age', Integer)\n",
    "    height = Column('height', Float)\n",
    "    weight = Column('weight', Float)\n",
    "    team = Column('team', String)\n",
    "    noc = Column(String, ForeignKey('NOCRegion.noc'))\n",
    "    games = Column('games', String) \n",
    "    year = Column('years', Integer)\n",
    "    season = Column('season', String)\n",
    "    city = Column('city', String)\n",
    "    sport = Column('sport', String)\n",
    "    event = Column('event', String)\n",
    "    medal = Column('medal', String)\n",
    "\n",
    "    # property\n",
    "    noc_region = relationship(\"NOCRegion\", back_populates=\"athlete_events\")\n",
    "\n",
    "    # methods\n",
    "    def __repr__(self):\n",
    "        return f'{self.name, self.noc, self.season, self.year, self.event, self.medal}'\n",
    "    \n",
    "    def __str__(self):\n",
    "        return self.__repr__() \n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 164,
   "id": "6fc23de1-163c-4228-8a68-20b333b47157",
   "metadata": {},
   "outputs": [],
   "source": [
    "class NOCRegion(Base):\n",
    "    __tablename__ = 'NOCRegion'\n",
    "\n",
    "    # columns\n",
    "    noc = Column('noc', String, primary_key = True)\n",
    "    region = Column('region', String)\n",
    "    note = Column('note', String)\n",
    "\n",
    "    # property\n",
    "    athlete_events = relationship(\"AthleteEvent\", back_populates=\"noc_region\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 165,
   "id": "0371186f-4637-418b-baa7-76c36e32422e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2023-04-19 10:32:35,578 INFO sqlalchemy.engine.Engine select pg_catalog.version()\n",
      "2023-04-19 10:32:35,582 INFO sqlalchemy.engine.Engine [raw sql] {}\n",
      "2023-04-19 10:32:35,693 INFO sqlalchemy.engine.Engine select current_schema()\n",
      "2023-04-19 10:32:35,694 INFO sqlalchemy.engine.Engine [raw sql] {}\n",
      "2023-04-19 10:32:35,800 INFO sqlalchemy.engine.Engine show standard_conforming_strings\n",
      "2023-04-19 10:32:35,800 INFO sqlalchemy.engine.Engine [raw sql] {}\n",
      "2023-04-19 10:32:35,839 INFO sqlalchemy.engine.Engine BEGIN (implicit)\n",
      "2023-04-19 10:32:35,883 INFO sqlalchemy.engine.Engine SELECT pg_catalog.pg_class.relname \n",
      "FROM pg_catalog.pg_class JOIN pg_catalog.pg_namespace ON pg_catalog.pg_namespace.oid = pg_catalog.pg_class.relnamespace \n",
      "WHERE pg_catalog.pg_class.relname = %(table_name)s AND pg_catalog.pg_class.relkind = ANY (ARRAY[%(param_1)s, %(param_2)s, %(param_3)s, %(param_4)s, %(param_5)s]) AND pg_catalog.pg_table_is_visible(pg_catalog.pg_class.oid) AND pg_catalog.pg_namespace.nspname != %(nspname_1)s\n",
      "2023-04-19 10:32:35,884 INFO sqlalchemy.engine.Engine [generated in 0.00069s] {'table_name': 'AthleteEvent', 'param_1': 'r', 'param_2': 'p', 'param_3': 'f', 'param_4': 'v', 'param_5': 'm', 'nspname_1': 'pg_catalog'}\n",
      "2023-04-19 10:32:36,017 INFO sqlalchemy.engine.Engine SELECT pg_catalog.pg_class.relname \n",
      "FROM pg_catalog.pg_class JOIN pg_catalog.pg_namespace ON pg_catalog.pg_namespace.oid = pg_catalog.pg_class.relnamespace \n",
      "WHERE pg_catalog.pg_class.relname = %(table_name)s AND pg_catalog.pg_class.relkind = ANY (ARRAY[%(param_1)s, %(param_2)s, %(param_3)s, %(param_4)s, %(param_5)s]) AND pg_catalog.pg_table_is_visible(pg_catalog.pg_class.oid) AND pg_catalog.pg_namespace.nspname != %(nspname_1)s\n",
      "2023-04-19 10:32:36,017 INFO sqlalchemy.engine.Engine [cached since 0.1339s ago] {'table_name': 'NOCRegion', 'param_1': 'r', 'param_2': 'p', 'param_3': 'f', 'param_4': 'v', 'param_5': 'm', 'nspname_1': 'pg_catalog'}\n",
      "2023-04-19 10:32:36,019 INFO sqlalchemy.engine.Engine \n",
      "CREATE TABLE \"NOCRegion\" (\n",
      "\tnoc VARCHAR NOT NULL, \n",
      "\tregion VARCHAR, \n",
      "\tnote VARCHAR, \n",
      "\tPRIMARY KEY (noc)\n",
      ")\n",
      "\n",
      "\n",
      "2023-04-19 10:32:36,020 INFO sqlalchemy.engine.Engine [no key 0.00041s] {}\n",
      "2023-04-19 10:32:36,349 INFO sqlalchemy.engine.Engine \n",
      "CREATE TABLE \"AthleteEvent\" (\n",
      "\tathlete_event_id SERIAL NOT NULL, \n",
      "\tid INTEGER, \n",
      "\tname VARCHAR, \n",
      "\tage INTEGER, \n",
      "\theight FLOAT, \n",
      "\tweight FLOAT, \n",
      "\tteam VARCHAR, \n",
      "\tnoc VARCHAR, \n",
      "\tgames VARCHAR, \n",
      "\tyears INTEGER, \n",
      "\tseason VARCHAR, \n",
      "\tcity VARCHAR, \n",
      "\tsport VARCHAR, \n",
      "\tevent VARCHAR, \n",
      "\tmedal VARCHAR, \n",
      "\tPRIMARY KEY (athlete_event_id), \n",
      "\tFOREIGN KEY(noc) REFERENCES \"NOCRegion\" (noc)\n",
      ")\n",
      "\n",
      "\n",
      "2023-04-19 10:32:36,351 INFO sqlalchemy.engine.Engine [no key 0.00199s] {}\n",
      "2023-04-19 10:32:36,391 INFO sqlalchemy.engine.Engine COMMIT\n"
     ]
    }
   ],
   "source": [
    "# create tables\n",
    "Base.metadata.create_all(engine)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 167,
   "id": "3868058b-2890-45ec-b202-18d262260e8b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2023-04-19 10:48:30,857 INFO sqlalchemy.engine.Engine BEGIN (implicit)\n",
      "2023-04-19 10:48:30,859 INFO sqlalchemy.engine.Engine DELETE FROM \"AthleteEvent\" WHERE \"AthleteEvent\".name = %(name_1)s\n",
      "2023-04-19 10:48:30,859 INFO sqlalchemy.engine.Engine [cached since 37.66s ago] {'name_1': 'Yuto Horigome'}\n",
      "2023-04-19 10:48:30,884 INFO sqlalchemy.engine.Engine COMMIT\n",
      "2023-04-19 10:48:30,885 INFO sqlalchemy.engine.Engine BEGIN (implicit)\n",
      "2023-04-19 10:48:30,886 INFO sqlalchemy.engine.Engine DELETE FROM \"NOCRegion\" WHERE \"NOCRegion\".region = %(region_1)s\n",
      "2023-04-19 10:48:30,886 INFO sqlalchemy.engine.Engine [cached since 37.53s ago] {'region_1': 'Japan'}\n",
      "2023-04-19 10:48:30,887 INFO sqlalchemy.engine.Engine COMMIT\n",
      "2023-04-19 10:48:30,893 INFO sqlalchemy.engine.Engine BEGIN (implicit)\n",
      "2023-04-19 10:48:30,900 INFO sqlalchemy.engine.Engine INSERT INTO \"NOCRegion\" (noc, region, note) VALUES (%(noc)s, %(region)s, %(note)s)\n",
      "2023-04-19 10:48:30,901 INFO sqlalchemy.engine.Engine [generated in 0.00062s] {'noc': 'JPN', 'region': 'Japan', 'note': None}\n",
      "2023-04-19 10:48:30,930 INFO sqlalchemy.engine.Engine COMMIT\n",
      "2023-04-19 10:48:30,949 INFO sqlalchemy.engine.Engine BEGIN (implicit)\n",
      "2023-04-19 10:48:30,952 INFO sqlalchemy.engine.Engine INSERT INTO \"AthleteEvent\" (id, name, age, height, weight, team, noc, games, years, season, city, sport, event, medal) VALUES (%(id)s, %(name)s, %(age)s, %(height)s, %(weight)s, %(team)s, %(noc)s, %(games)s, %(years)s, %(season)s, %(city)s, %(sport)s, %(event)s, %(medal)s) RETURNING \"AthleteEvent\".athlete_event_id\n",
      "2023-04-19 10:48:30,953 INFO sqlalchemy.engine.Engine [generated in 0.00151s] {'id': None, 'name': 'Yuto Horigome', 'age': 21, 'height': None, 'weight': None, 'team': 'Japan', 'noc': 'JPN', 'games': None, 'years': 2020, 'season': 'Summer', 'city': 'Tokyo', 'sport': 'Skateboarding', 'event': 'Skatboarding, Street, Men', 'medal': 'Gold'}\n",
      "2023-04-19 10:48:31,005 INFO sqlalchemy.engine.Engine COMMIT\n"
     ]
    }
   ],
   "source": [
    "# This part is used to delete previously added objects for testing purpose\n",
    "session.query(AthleteEvent).filter(AthleteEvent.name==\"Yuto Horigome\").delete()\n",
    "session.commit()\n",
    "session.query(NOCRegion).filter(NOCRegion.region==\"Japan\").delete()\n",
    "session.commit()\n",
    "r = NOCRegion(noc = 'JPN', region = 'Japan')\n",
    "session.add(r)\n",
    "session.commit()\n",
    "\n",
    "a = AthleteEvent(\n",
    "    name = \"Yuto Horigome\", age = 21, team = 'Japan', medal = 'Gold', year = 2020, season = 'Summer', \n",
    "    city = 'Tokyo', noc = 'JPN', sport = 'Skateboarding', event = 'Skatboarding, Street, Men')\n",
    "session.add(a)\n",
    "session.commit()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 168,
   "id": "ea9db37b-9259-456a-93c6-cf5df6090d27",
   "metadata": {},
   "outputs": [],
   "source": [
    "result = session.query(AthleteEvent).filter(\n",
    "    AthleteEvent.noc == 'JPN', \n",
    "    AthleteEvent.year >= 2016,\n",
    "    AthleteEvent.medal == 'Gold')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 169,
   "id": "fe496862-adc6-4aff-922c-9f94ca90b69c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2023-04-19 10:51:11,991 INFO sqlalchemy.engine.Engine BEGIN (implicit)\n",
      "2023-04-19 10:51:12,007 INFO sqlalchemy.engine.Engine SELECT \"AthleteEvent\".athlete_event_id AS \"AthleteEvent_athlete_event_id\", \"AthleteEvent\".id AS \"AthleteEvent_id\", \"AthleteEvent\".name AS \"AthleteEvent_name\", \"AthleteEvent\".age AS \"AthleteEvent_age\", \"AthleteEvent\".height AS \"AthleteEvent_height\", \"AthleteEvent\".weight AS \"AthleteEvent_weight\", \"AthleteEvent\".team AS \"AthleteEvent_team\", \"AthleteEvent\".noc AS \"AthleteEvent_noc\", \"AthleteEvent\".games AS \"AthleteEvent_games\", \"AthleteEvent\".years AS \"AthleteEvent_years\", \"AthleteEvent\".season AS \"AthleteEvent_season\", \"AthleteEvent\".city AS \"AthleteEvent_city\", \"AthleteEvent\".sport AS \"AthleteEvent_sport\", \"AthleteEvent\".event AS \"AthleteEvent_event\", \"AthleteEvent\".medal AS \"AthleteEvent_medal\" \n",
      "FROM \"AthleteEvent\" \n",
      "WHERE \"AthleteEvent\".noc = %(noc_1)s AND \"AthleteEvent\".years >= %(years_1)s AND \"AthleteEvent\".medal = %(medal_1)s\n",
      "2023-04-19 10:51:12,009 INFO sqlalchemy.engine.Engine [generated in 0.00136s] {'noc_1': 'JPN', 'years_1': 2016, 'medal_1': 'Gold'}\n",
      "2023-04-19 10:51:12,064 INFO sqlalchemy.engine.Engine SELECT \"NOCRegion\".noc AS \"NOCRegion_noc\", \"NOCRegion\".region AS \"NOCRegion_region\", \"NOCRegion\".note AS \"NOCRegion_note\" \n",
      "FROM \"NOCRegion\" \n",
      "WHERE \"NOCRegion\".noc = %(pk_1)s\n",
      "2023-04-19 10:51:12,065 INFO sqlalchemy.engine.Engine [generated in 0.00055s] {'pk_1': 'JPN'}\n",
      "('Yuto Horigome', 'Japan', 'Skatboarding, Street, Men', 2020, 'Summer')\n",
      "Yuto Horigome\n",
      "Japan\n",
      "Skatboarding, Street, Men\n",
      "2020\n",
      "Summer\n"
     ]
    }
   ],
   "source": [
    "# display results\n",
    "for r in result:\n",
    "    print(f'{r.name,r.noc_region.region,r.event,r.year,r.season}')\n",
    "    print(r.name)\n",
    "    print(r.noc_region.region)\n",
    "    print(r.event)\n",
    "    print(r.year)\n",
    "    print(r.season)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 149,
   "id": "7c9192e6-7f46-483b-90f5-1c32369b81c0",
   "metadata": {},
   "outputs": [],
   "source": [
    "session.close()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1e6710da-4374-487e-8e71-307b7c979ed0",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a92cc7e2-3030-41fe-be32-173cdbf33326",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
