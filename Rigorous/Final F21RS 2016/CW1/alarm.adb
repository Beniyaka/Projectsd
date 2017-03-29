package body Alarm
is
	State: Boolean;

	procedure Enable
	is
	begin
		State := true;
	end Enable;

	procedure Disable
	is
	begin
		State := false;
	end Disable;

	function Enabled return Boolean
	is
	begin
		return State;
	end Enabled;
begin
	State := false;
end Alarm;
