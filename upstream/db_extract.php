<?php
    $dbhost = 'localhost';
    $dbuser = 'root';
    $dbpass = 'asdf';
    $dbname = 'sugar_7_7_ent';
    $jsonfile = '/tmp/dump.json';
    $conn = new mysqli($dbhost, $dbuser, $dbpass, $dbname);
    if ($conn->connect_error) {
        die("Connection failed: " . $conn->connect_error);
    } 
    $fields = ['salutation', 'title', 'facebook', 'twitter', 'googleplus', 'department', 'account_id', 'tag', 'lead_source', 'preferred_language', 'campaign_id'];
    $sql = "SELECT status, " . implode(', ', $fields) . " FROM leads";
    $result = $conn->query($sql);
    $output = array();
    // go through each row from the db
    while ($row = $result->fetch_assoc()) {
        // we're using the status field as our grouping parameter
        $status = $row['status'];
        if (!$output[$status]) {
            $output[$status] = array();
            $output[$status]['count'] = 0;
        }
        // go through each field from the results and capture it in the appropriate place
        foreach ($fields as $field) {
            if (!$output[$status][$field]) {
                $output[$status][$field] = array();
            }
            $output[$status][$field][] = $row[$field];
        }
        $output[$status]['count']++;
    }
    $conn->close();
    $writehandle = fopen($jsonfile, 'w');
    fwrite($writehandle, json_encode($output));
    fclose($writehandle);
?>
