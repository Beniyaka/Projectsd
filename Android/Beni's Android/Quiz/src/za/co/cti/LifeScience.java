package za.co.cti;

import java.util.Vector;

import android.app.Activity;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.view.View.OnClickListener;
import android.widget.Button;
import android.widget.RadioButton;
import android.widget.RadioGroup;
import android.widget.TextView;
import android.widget.Toast;

public class LifeScience 
extends Activity
implements OnClickListener {
	private TextView question;
	private TextView summary;
	private Vector<MCQuestion> questions;
	private RadioGroup opts;
	private MCQuestion currentQuestion;
	private int noCorrect;
	private int noAnswered;
	private int noQuestions = 3;
	
    /** Called when the activity is first created. */
    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.multichoice);
        Log.i("MCQ", "MultiChoice starts");
        opts = (RadioGroup) findViewById(R.id.opts);
        Button sub = (Button) findViewById(R.id.submit);
        question = (TextView) findViewById(R.id.question_text);
        summary = (TextView) findViewById(R.id.multichoice_summary);  
        noCorrect = 0;
        noAnswered = 0;
        sub.setOnClickListener(this);
        initialiseQuestions();
        generateSummary();
        generateQuestion(0);
    }

	private void generateQuestion(int noQ) {
		opts.removeAllViews();
		currentQuestion = questions.get(noQ);
		question.setText(currentQuestion.getQuestion());
		int i = 1;
		for( String ans: currentQuestion.getAnswers()) {
			RadioButton rb = new RadioButton(this);
			rb.setText(ans);
			rb.setId(i++);
			opts.addView(rb);
		}
	}

	private void initialiseQuestions() {
		questions = new Vector<MCQuestion>();
		MCQuestion q1 = new MCQuestion("Which term represent the contact force that a surface act on an object?");
		q1.addAnswer("Unbalanced force", false);
		q1.addAnswer("Friction", true);
		q1.addAnswer("Banlanced force", false);
		questions.add(q1);	
		q1 = new MCQuestion("What is the general equation of Potassium Chloride?");
		q1.addAnswer("NaCl", false);
		q1.addAnswer("KCl", true);
		q1.addAnswer("HCl", false);
		questions.add(q1);	
		q1 = new MCQuestion("Which is a common acid?");
		q1.addAnswer("Sulphuric acid", true);
		q1.addAnswer("Metal Oxide", false);
		q1.addAnswer("Red onion water", false);
		questions.add(q1);	
		// more questions could be added
		}
	
	   private void generateSummary()
	    {
	    	summary.setText( noCorrect + " answers out of " + noAnswered 
	    			+ " attempted of " +noQuestions + " questions");
	    }

	public void onClick(View arg0) {
		noAnswered++;
		int id;
		id = opts.getCheckedRadioButtonId();
		if( currentQuestion.isCorrect(id))
			noCorrect++;
		generateSummary();
		if (noAnswered == noQuestions)
			finish();
		else
			generateQuestion(noAnswered);
	}
}