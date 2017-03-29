package za.co.cti;

import android.app.Activity;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.view.View.OnClickListener;
import android.widget.Button;
import android.widget.TextView;
import android.widget.Toast;
import android.content.Intent;

public class QuizActivity 
	extends Activity
	implements OnClickListener
{
	private Button historyButton;
	private Button mathsButton;
	private Button lifescience;
	private TextView summary;
    /** Called when the activity is first created. */
    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.main);
        
        lifescience = (Button) findViewById(R.id.lifescience_button);
        lifescience.setOnClickListener(this);
        historyButton = (Button) findViewById(R.id.history);
        historyButton.setOnClickListener(this);
        summary = (TextView) findViewById(R.id.overall_summary);
        mathsButton = (Button) findViewById(R.id.maths_button);
        mathsButton.setOnClickListener(this);
   }
    
	public void onClick(View arg0)
	{
		
		if ( arg0 == lifescience ) {
			Log.i("QUIZ", "History selected");
			Toast.makeText(getApplicationContext(), "Physical Science button pressed", Toast.LENGTH_LONG).show();
			Intent intent = new Intent(QuizActivity.this,LifeScience.class);
			QuizActivity.this.startActivity(intent);
		}
		if ( arg0 == mathsButton ) {
			Log.i("QUIZ", "Maths selected");
			Toast.makeText(getApplicationContext(), "Maths button pressed", Toast.LENGTH_LONG).show();
			Intent intent = new Intent(QuizActivity.this,MathsQuestionsActivity.class);
			QuizActivity.this.startActivity(intent);
		}
		if ( arg0 == historyButton ) {
			Log.i("QUIZ", "Geography selected");
			Toast.makeText(getApplicationContext(), "Geography button pressed", Toast.LENGTH_LONG).show();
			Intent intent = new Intent(QuizActivity.this,MultiChoiceQuestionsActivity.class);
			QuizActivity.this.startActivity(intent);
		}
	}
}