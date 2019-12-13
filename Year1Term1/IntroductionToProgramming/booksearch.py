import database as db

def go(target = ""):
    result = []
    # first try if input is an id
    result.extend(db.search_by_id(target))
    # they try if input is book name (highly unlikely to be both at once)
    result.extend(db.search_by_name(target))
    # add log entry
    return result
