instructions=[
    'SET FOREIGN_KEY_CHECKS=0;',
    'DROP TABLE IF EXISTS todo;',
    'DROP TABLE IF EXISTS user;',
    'SET FOREIGN_KEY_CHECKS=1;',
    """
        CREATE TABLE user(
            id serial NOT NULL,
            username character varying(50) NOT NULL,
            password character varying(100) NOT NULL,
            PRIMARY KEY (id)
        )
    """,
    """
        CREATE TABLE todo(
            id serial NOT NULL,
            created_by numeric NOT NULL,
            created_at date NOT NULL,
            description text NOT NULL,
            completed boolean NOT NULL,
            PRIMARY KEY (id),
            CONSTRAINT fk_created_by FOREIGN KEY (created_by)
                REFERENCES public.test (id) MATCH SIMPLE
        )
    """,
]