"""Database comparison feature tests."""

from pytest_bdd import (
    given,
    scenarios,
    then,
    when,
    parsers
)

from tests.pageobjects.db_comparison import DBComparison

scenarios('../features/db.feature')


@given(parsers.parse('connection is established between source and target databases'))
def connection_is_established_between_source_and_target_databases(driver, conn_list):
    """connection is established between source and target databases."""
    db = DBComparison()
    print('DB IS CONNECTED')
    pass


@when(parsers.parse('user executes "<query1>" on source and "<query2>" on target databases'))
def user_executes_query_on_source_and_on_target_databases(db, conn1, conn2, query1, query2):
    """user executes "<query1>" on source and "<query2>" on target databases."""
    # db = DBComparison()
    tables_frames = db.execute_query(conn1, conn2, query1, query2)


@when(parsers.parse('results from both database resultsets are compared'))
def results_from_both_database_resultsets_are_compared(db, conn1, conn2, tables_frames):
    """results from both database resultsets are compared."""
    # db = DBComparison()
    results = db.compare_tables(tables_frames)


@then(parsers.parse('user reports any mismatches'))
def user_reports_any_mismatches(results):
    """user reports any mismatches."""
    print('This is dataframe1\n')
    print(results[0])
    print('This is dataframe2\n')
    print(results[1])
