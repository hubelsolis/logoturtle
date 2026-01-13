program TurtleUNAS;

uses
  Vcl.Forms,
  umain in 'umain.pas' {Form8},
  OPERADORESmini in '..\SHARED\OPERADORESmini.PAS',
  uencriptar in '..\SHARED\uencriptar.pas',
  Vcl.Themes,
  Vcl.Styles;

{$R *.res}

begin
  Application.Initialize;
  Application.MainFormOnTaskbar := True;
  TStyleManager.TrySetStyle('Sky');
  Application.CreateForm(TForm8, Form8);
  Application.Run;
end.
