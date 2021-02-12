import { ComponentFixture, TestBed } from '@angular/core/testing';

import { TableResumeVHLComponent } from './table-resume-vhl.component';

describe('TableResumeVHLComponent', () => {
  let component: TableResumeVHLComponent;
  let fixture: ComponentFixture<TableResumeVHLComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ TableResumeVHLComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(TableResumeVHLComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
