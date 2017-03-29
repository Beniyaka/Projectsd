with Brakes, Alarm;
package body Console
is
	--hidden from packages using console
	Reset_Status: Boolean;
	SPAD_Cnt: SPAD_Cnt_SubType;

	procedure Enable_Reset
	is
	begin
		Reset_Status := true;
	end Enable_Reset;

	procedure Disable_Reset
	is
	begin
		Reset_Status := false;
	end Disable_Reset;

	function Reset_Enabled return Boolean
	is
	begin
		return Reset_Status;
	end Reset_Enabled;

	procedure Inc_SPAD_Cnt
	is
	begin
		if SPAD_Cnt < SPAD_Cnt_SubType'Last then
		--# check SPAD_Cnt + 1 in Integer;
		SPAD_Cnt := SPAD_Cnt + 1;
		end if;
	end Inc_SPAD_Cnt;

	procedure Reset_SPAD_Cnt
	is
	begin
		SPAD_Cnt := 0;
	end Reset_SPAD_Cnt;

	function SPAD_Cnt_Value return Integer
	is
	begin
		return SPAD_Cnt;
	end SPAD_Cnt_Value;
begin
	Reset_Status := false;
	SPAD_Cnt := 0;
end Console;
