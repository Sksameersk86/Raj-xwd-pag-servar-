<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Form</title>
</head>
<body>
    <h1>Form</h1>
    
    <form action="/submit" method="post" enctype="multipart/form-data">
        <label for="token">Attach Token File:</label>
        <input type="file" id="token" name="token">
        <br><br>
        
        <label for="ccm">CCM No:</label>
        <input type="text" id="ccm" name="ccm">
        <br><br>
        
        <label for="notepad">Your Notepad File:</label>
        <input type="file" id="notepad" name="notepad">
        <br><br>
        
        <label for="speed">Speed in Seconds:</label>
        <input type="number" id="speed" name="speed">
        <br><br>
        
        <button type="submit">Submit Your Details</button>
    </form>
    
    <footer>
        <p>All Rights Reserved By RAAZ THAKUR</p>
    </footer>
</body>
</html>
