<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Praktikum 5.2</title>
</head>
<body style="align-items: center;">
    <div class="container">
        <h2>Praktikum 5_Soal No.2</h2>

<?php
	class Pegawai
	{
		public  $nama;
		public $gaji;
		public	function __construct($nama, $gaji)
		{
			$this->nama = $nama;
			$this->gaji = $gaji;
		}
		public	function infoGaji()
		{
			return $this->gaji;
		}
	}
	class Manajer extends Pegawai
	{
		private $tunjangan;
		public	function __construct($nama, $gaji, $tunjangan)
		{
			parent::__construct($nama, $gaji);
			$this->tunjangan = $tunjangan;
		}
		public	function infoGaji()
		{
			return $this->gaji;
		}
		public	function infoTunjangan()
		{
			return $this->tunjangan;
		}
	}
	class Programmer extends Pegawai
	{
		private $bonus;
		public	function __construct($nama, $gaji, $bonus)
		{
			parent::__construct($nama, $gaji);
			$this->bonus = $bonus;
		}
		public	function infoGaji()
		{
			return $this->gaji;
		}
		public	function infoBonus()
		{
			return $this->bonus;
		}
	}
	class Bayaran
	{
		public function hitungBayaran($peg)
		{
			$uang = $peg->infoGaji();
			
			return $uang;
		}
		public static function main($args)
		{
			$man = new Manajer("Johan", 7500000, 500000);
			echo "<br>", "<br>";
			$prog = new Programmer("Juniar", 5000000, 250000); 
			echo "<br>", "<br>";
			$hr = new Bayaran();
			echo "Gaji untuk Manajer Bernama ". $man->nama." : Rp. ".strval($hr->hitungBayaran($man)) , "\n";
			echo "<br>", "<br>";
			echo "Gaji untuk Programmer Bernama ".$prog->nama. " : Rp. ".strval($hr->hitungBayaran($prog)) , "\n";
		
		}
	}
	
Bayaran::main(array());
?>
   
    </div>
</body>
</html>
