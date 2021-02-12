import { ComponentFixture, TestBed } from '@angular/core/testing';

import { TableResumeEffComponent } from './table-resume-eff.component';

describe('TableResumeEffComponent', () => {
  let component: TableResumeEffComponent;
  let fixture: ComponentFixture<TableResumeEffComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ TableResumeEffComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(TableResumeEffComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
