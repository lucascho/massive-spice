<?php
    $jsonfile = "/tmp/dump.json";
    $readhandle = fopen('/tmp/dump.json', 'r');
    $json = fread($readhandle, filesize($jsonfile));
    $dataStruct = json_decode($json, true);
    foreach ($dataStruct as $key => $value) {
        echo "$key " . $dataStruct[$key]['count'] . "\n";
    }
?>
