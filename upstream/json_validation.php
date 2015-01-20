<?php
    $jsonfile = "/tmp/dump.json";
    $fields = ['salutation', 'title', 'facebook', 'twitter', 'googleplus', 'department', 'account_id', 'tag', 'lead_source', 'preferred_language', 'campaign_id'];
    $readhandle = fopen('/tmp/dump.json', 'r');
    $json = fread($readhandle, filesize($jsonfile));
    $dataStruct = json_decode($json, true);
    foreach ($dataStruct as $key => $value) {
        echo "$key " . $dataStruct[$key]['count'] . "\n";
    }
?>
