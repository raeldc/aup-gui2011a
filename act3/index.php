<!DOCTYPE html>
<head>
    <title>GUI Programming - Manipulating Values of the DOM Element</title>
    <script type="text/javascript" src="https://ajax.googleapis.com/ajax/libs/mootools/1.3.2/mootools-yui-compressed.js"></script>
    <script type="text/javascript" src="js/app.js"></script>
    <link rel="stylesheet" href="css/reset.css" type="text/css" media="screen" title="Reset CSS" charset="utf-8">
</head>
<body>
    <form name="students-table" method="post" action="">
        <table id="students">
            <tr>
                <th>&nbsp;</th>
                <th>Name</th>
                <th>Score</th>
            </tr>
            <tbody>
            </tbody>
            
            <tfooter>
                <td colspan="2"><input type="text" value="" name="name" id="name-textbox" /></td>
                <td>
                    <input type="text" value="" name="score" id="score-textbox" />
                    <input type="button" value="Add" id="add-button" />
                </td>
            </tfooter>
        </table>
        <p>Average Score is: <span id="average-textbox">0</span></p>
    </form>
</body>