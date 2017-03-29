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
	private int noQuestions = 4;
	
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
		MCQuestion q1 = new MCQuestion("Who won the Battle of Hastings?");
		q1.addAnswer("Harold Godwinson", false);
		q1.addAnswer("William of Normandy", true);
		q1.addAnswer("Edward the Confessor", false);
		q1.addAnswer("Harald Hadrada", false);
		questions.add(q1);	
		q1 = new MCQuestion(">Who won the Battle of Waterloo?");
		q1.addAnswer("Wellington", true);
		q1.addAnswer("Napoleon", false);
		q1.addAnswer("Blucher", false);
		q1.addAnswer("Marlborough", false);
		questions.add(q1);	
		q1 = new MCQuestion("Who was the first Roman emperor?");
		q1.addAnswer("Augustus", true);
		q1.addAnswer("Julius Caesar", false);
		q1.addAnswer("Nero", false);
		q1.addAnswer("Trajan", false);
		questions.add(q1);	
		q1 = new MCQuestion("Which Roman emperor built a wall across Scotland?");
		q1.addAnswer("Antonius", true);
		q1.addAnswer("Hadrianr", false);
		q1.addAnswer("Trajan", false);
		q1.addAnswer("Constantine", false);
		questions.add(q1);			}
	
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