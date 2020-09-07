from tableqa.clauses import Clause
import pytest
import os
clause=Clause()
def test_Clause():
    types={"SELECT {} FROM {}":["which are the activities in 2011","find who died of stomach cancer"],
           "SELECT MAX({}) FROM {}":["find the highest gdp value","when was the most number of cases reported","what was the maximum age of stomach cancer patients"],
           "SELECT MIN({}) FROM {}":["find the lowest gdp value","when was the least number of cases reported","what was the minimum age of stomach cancer patients"],
           "SELECT COUNT({}) FROM {}":["how many men died of stomach cancer in 2011","Find the number of activities in this data","Amount of people who died of cancer"],
           "SELECT SUM({}) FROM {}":["sum of all cases","sum of death count"],
           "SELECT AVG({}) FROM {}":["what is the average gdp last year","find the average number of reported cases","get me the average number of reported cases"]}
    for key,typ in types.items():
        for q in typ:
            print(q,clause.adapt(q))
            assert clause.adapt(q) == key 



if __name__ == '__main__':
    pytest.main([__file__])
    
