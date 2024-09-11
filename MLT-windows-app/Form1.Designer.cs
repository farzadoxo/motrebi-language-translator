namespace MLT_windows_app;

partial class Form1
{
    /// <summary>
    ///  Required designer variable.
    /// </summary>
    private System.ComponentModel.IContainer components = null;

    /// <summary>
    ///  Clean up any resources being used.
    /// </summary>
    /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
    protected override void Dispose(bool disposing)
    {
        if (disposing && (components != null))
        {
            components.Dispose();
        }
        base.Dispose(disposing);
    }

    #region Windows Form Designer generated code

    /// <summary>
    ///  Required method for Designer support - do not modify
    ///  the contents of this method with the code editor.
    /// </summary>
    private void InitializeComponent()
    {
        this.components = new System.ComponentModel.Container();
        this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
        this.ClientSize = new System.Drawing.Size(600, 450);
        this.Text = "🎷MLT 0.1";



        // Define components properties
        headerLabel = new Label
        {
            Text = "Welcome to MLT 👋",
            ForeColor = Color.Blue,
            Location = new Point(2,2),
            Size = new Size(100,50)
        };


        // Locating (place) objects and components
        this.Controls.Add(headerLabel);
    }


    // Define components
    // --------------------------
    private Label headerLabel;
    private Label inputLabel;
    private Label outputLabel;
    private TextBox inputTextBox;
    private TextBox outputTextBox;
    private Button translateButton;


    #endregion
}
