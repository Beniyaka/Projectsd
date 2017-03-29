package counter
--# own my_counter;
--# initializes my_counter;
is
	procedure Increment;
	--# global in out my_counter;

	procedure Decrement;
	--# global in out my_counter;

	function Value return Integer;
	--# global in my_counter;

	procedure Reset(AValue: in Integer);
	--# global out my_counter;
	--# derives my_counter from AValue;
end counter;
