<?php
// Data input untuk API
$data = [
    "Kode_Mk" => "TT19111",
    "Id_Dosen" => 147
];

// Konversi data menjadi JSON
$data_string = json_encode($data);

// Inisialisasi CURL
$ch = curl_init('http://127.0.0.1:5000/predict');
curl_setopt($ch, CURLOPT_CUSTOMREQUEST, "POST");
curl_setopt($ch, CURLOPT_POSTFIELDS, $data_string);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_HTTPHEADER, [
    'Content-Type: application/json',
    'Content-Length: ' . strlen($data_string)
]);

// Eksekusi API dan ambil hasilnya
$response = curl_exec($ch);
curl_close($ch);

// Decode hasil API
$result = json_decode($response, true);

// Tampilkan hasil
echo "Slot Hari: " . $result['Slot_Hari'] . "<br>";
echo "Slot Waktu: " . $result['Slot_Waktu'] . "<br>";
echo "Ruangan: " . $result['Ruangan'] . "<br>";
?>
