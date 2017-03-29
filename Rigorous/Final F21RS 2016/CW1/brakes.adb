package body Brakes
is
	State: boolean;

	procedure Activate
	is
	begin
		State := true;
	end Activate;

	procedure Deactivate
	is
	begin
		State := false;
	end Deactivate;

	function Activated return Boolean
	is
	begin
		return State;
	end Activated;
begin
	State := false;
end Brakes;
