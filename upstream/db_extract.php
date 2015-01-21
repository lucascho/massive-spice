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
    $fields = array(
        "date_entered" => "date",
        "date_modified" => "date",
        "description" => "numeric",
        "opportunity_type" => "string",
        "campaign_id" => "string",
        "lead_source" => "string",
        "amount" => "numeric",
        "base_rate" => "numeric",
        "amount_usdollar" => "numeric",
        "currency_id" => "string",
        "date_closed" => "date",
        "next_step" => "string",
        "probability" => "numeric",
        "best_case" => "numeric",
        "worst_case" => "numeric",
        "commit_stage" => "string",
        "total_revenue_line_items" => "numeric",
        "closed_revenue_line_items" => "numeric",
    );
    $sql = "SELECT sales_stage, " . implode(', ', array_keys($fields)) . " FROM opportunities";
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
        foreach ($fields as $field => $type) {
            if (!$output[$status][$field]) {
                $output[$status][$field] = array(
                    "type" => $type,
                    "values" => array(),
                );
            }
            $value = $row[$field];
            if ($field == "description") {
                $value = strlen($value);
            }
            $output[$status][$field]['values'][] = $value;
        }
        $output[$status]['count']++;
    }
    $conn->close();
    $writehandle = fopen($jsonfile, 'w');
    fwrite($writehandle, json_encode($output));
    fclose($writehandle);
?>
