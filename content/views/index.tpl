<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="Pragma" content="no-cache">
        <meta http-equiv="Cache-Control" content="no-cache">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
        <title>List</title>
        <!-- load css files -->
        <!-- <link rel="stylesheet" href="static/css/bootstrap.min.css"> -->
    </head>
    <body>      
        <main>
        <h1>Door_Open_Log</h1>
        <div>
            <h3>Logs</h3>
		<table border="1">
    		    <tr>
      			<th>日付</th>
			<th>ドア情報</th>
    		    </tr>
           	     % for log in req["log"]:
		     <tr>
	        	<td>{{ log["date_at"] }}</td>
			<td>{{ log["is_open"] }}</td>
		    </tr>
	            % end
		</table>
        </div>
        </main>
        <!-- load script files -->
        <!-- script type="text/javascript" src="static/js/caller.js" charset="utf-8"></script -->
    </body>
</html>
