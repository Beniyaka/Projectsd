
with Text_IO, ASM_Int_Stack;
use Text_IO, ASM_Int_Stack;

procedure Use_ASM_Int_Stack is

package Integer_INOUT is new Integer_IO(Integer);
   use Integer_INOUT;
package Boolean_INOUT is new Enumeration_IO(Boolean);
   use Boolean_INOUT;

   Op_Code: Integer;
   Data: Integer;

begin
   loop
      Put("1 = Push; 2 = Pop; 3 = Empty; 4 = Full: ");
      Get(Op_Code);
      case Op_Code is
         when 1 => Put("Data: "); Get(Data);
                   Push(Data);
         when 2 => Pop(Data);
                   Put(Data);New_Line;
         when 3 => Put(Empty);
                   New_Line;
         when 4 => Put(Full);
                   New_Line;
         when others => Put_Line("Error");
      end case;
   end loop;
end Use_ASM_Int_Stack;
