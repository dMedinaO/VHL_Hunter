import { ComponentFixture, TestBed } from '@angular/core/testing';

import { SwalSequencesComponent } from './swal-sequences.component';

describe('SwalSequencesComponent', () => {
  let component: SwalSequencesComponent;
  let fixture: ComponentFixture<SwalSequencesComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ SwalSequencesComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(SwalSequencesComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
