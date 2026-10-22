|#|	Fixture|	        Test body|	    Result|
|-| -------|--------|--------|
|1|	newtx_events|	append `"INSERT"`	|passes|
|2|	newtx_events|   append `"INSERT"`, then `assert False`	|fails (xfail)|
|3|	rollback_events|append `"INSERT"`	|passes|
|4|	rollback_events|append `"INSERT"`, then `assert False`	|fails (xfail)|