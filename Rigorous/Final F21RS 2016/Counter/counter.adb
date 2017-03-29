package body counter
is
	my_counter: Integer;

	procedure Increment is
	begin
		my_counter := my_counter + 1;
	end Increment;

	procedure Decrement is
	begin
		my_counter := my_counter - 1;
	end Decrement;

	function Value return Integer is
	begin
		return my_counter;
	end Value;

	procedure Reset(AValue: in Integer) is
	begin
		my_counter := AValue;
	end Reset;

begin
	my_counter:=0;

end counter;
