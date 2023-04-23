Feature: CRUD Operations
  As a user of the CRUD module
  I want to perform various CRUD operations on a MySQL database
  So that I can create, read, update, and delete data in the database

  Background:
    Given the database contains the following test data
      | Symbol | Price  | MarketCap  | MagicformulaIndex | AquirersMultiple |
      | AAPL   | 150.25 | 2500000000 | 5                 | 10               |
      | GOOGL  | 2150.35| 1500000000 | 8                 | 7                |
      | ...    | ...    | ...        | ...               | ...              |

  Scenario Outline: Insert data into an existing table
    Given an existing table "test"
    When I call the insert method with the data
      | Symbol | Price  | MarketCap  | MagicformulaIndex | AquirersMultiple |
      | <Symbol> | <Price> | <MarketCap> | <MagicformulaIndex> | <AquirersMultiple> |
    Then the data should be inserted into the specified table

    Examples:
      | Symbol | Price  | MarketCap  | MagicformulaIndex | AquirersMultiple |
      | NEW1   | 100.00 | 3000000000 | 3                 | 5                |
      | NEW2   | 200.00 | 3500000000 | 4                 | 6                |

  Scenario Outline: Read data from an existing table
    Given an existing table "test"
    When I call the read method with the condition "Symbol = '<Symbol>'"
    Then the data returned should be
      | Symbol | Price  | MarketCap  | MagicformulaIndex | AquirersMultiple |
      | <Symbol> | <Price> | <MarketCap> | <MagicformulaIndex> | <AquirersMultiple> |

    Examples:
      | Symbol | Price  | MarketCap  | MagicformulaIndex | AquirersMultiple |
      | AAPL   | 150.25 | 2500000000 | 5                 | 10               |
      | GOOGL  | 2150.35| 1500000000 | 8                 | 7                |

  Scenario Outline: Update data in an existing table
    Given an existing table "test"
    When I call the update method with the set_data and the condition "Symbol = '<Symbol>'"
      | Price  | MarketCap  | MagicformulaIndex | AquirersMultiple |
      | <Price> | <MarketCap> | <MagicformulaIndex> | <AquirersMultiple> |
    Then the data in the specified table should be updated

    Examples:
      | Symbol | Price  | MarketCap  | MagicformulaIndex | AquirersMultiple |
      | AAPL   | 151.00 | 2600000000 | 6                 | 11               |
      | GOOGL  | 2160.00| 1600000000 | 9                 | 8                |

  Scenario Outline: Delete data from an existing table
    Given an existing table "test"
    When I call the delete method with the condition "Symbol = '<Symbol>'"
    Then the data with the specified symbol should be deleted from the table

    Examples:
      | Symbol |
      | AAPL   |
      | GOOGL  |

  Scenario: Drop a table
    Given an existing table "test"
    When I call the drop_table method
    Then the specified table should be dropped from the database

