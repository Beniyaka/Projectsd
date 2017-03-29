package body Speedo
is
	Speed: Speed_Type;

	procedure Write_Speed(S: in Speed_Type)
	is
	begin
		Speed := S;
	end Write_Speed;

	function Read_Speed return Speed_Type
	is
	begin
		return Speed;
	end Read_Speed;

	begin
		Speed := 0;
end Speedo;
